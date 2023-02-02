from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from api.v1.auth.serializer import Userserializer
from api.models import User


class AuthView(GenericAPIView):
    serializer_class = Userserializer

    def post(self, request, *args, **kwargs):

        global user
        data = request.data
        method = data.get('method')
        params = data.get('params')

        if not method:
            return Response({
                "Error": "method kiritilmagan"
            })

        if params is None:
            return Response({
                "Error": "params kiritilmagan"
            })

        if method == "regis":
            mobile = params.get("mobile")
            user = User.objects.filter(mobile=mobile).first()

            if user:
                return Response({
                    "Error": "Bu tel nomer allaqachon bor"
                })

            serializer = self.get_serializer(data=params)
            serializer.is_valid(raise_exception=True)
            user = serializer.create(serializer.data)
            user.set_password(params["password"])
            user.save()

            # token = Token()
            # token.user = user
            # token.save()

            return Response({
                "result": {
                    "name": user.name,
                    "mobile": user.mobile,
                    "email": user.email
                }
            })

        elif method == "login":
            nottt = "email" if "email" not in params else "password" if "password" not in params else None
            nott = 'mobile' if 'mobile' not in params else "password" if "password" not in params else None

            if nott and nottt:
                return Response({
                    "Error": f"{nott} kiritilishi shart"
                })

            email = params.get("email")
            mobile = params.get("mobile")
            if mobile:
                user = User.objects.filter(mobile=mobile).first()
            if email:
                user = User.objects.filter(email=email).first()

            if not user:
                return Response({
                    "Error": "Bunday User topilmadi"
                })
            if not user.check_password(params['password']):
                return Response({
                    "Error": "parol  xato"
                })
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token()
                token.user = user
                token.save()
            # login(request, user)
            return Response({
                "result": {
                    "token": token.key,
                    "name": user.name,
                    "mobile": user.mobile,
                    "email": user.email,

                }
            })
        else:
            return Response({
                "Error": "Bunday method yoq"
            })

        # elif method == "step.one":
        #     nott = 'mobile' if "mobile" not in params else "lang" if "lang" not in params else None
        #     if nott:
        #         return Response({
        #             "Error": f"params.{nott} polyasi to'ldirilmagan"
        #
        #         })
        #
        #     code = random.randint(10000, 99999)
        #     otp = code_decoder(code)
        #     users = User.objects.filter(mobile=params["mobile"]).first()
        #     if users:
        #         return Response(
        #             {
        #                 'Error': "Bunday mobile allaqachon ro'yxatdan  o'tgan"
        #             }, status=status.HTTP_400_BAD_REQUEST
        #         )
        #     sms = sms_sender(params['mobile'], code, params['lang'])
        #     if sms.get('status') != "waiting":
        #         return Response({
        #             "error": "sms xizmatida qandaydir muommo",
        #             "data": sms
        #         })
        #
        #     root = OTP()
        #     root.mobile = params['mobile']
        #     root.key = uuid.uuid4().__str__() + "$" + otp + "$" + uuid.uuid1().__str__()
        #     root.save()
        #
        #     return Response({
        #         "otp": code,
        #         "token": root.key
        #     }
        #     )
        #
        # elif method == "step.two":
        #     nott = 'otp' if "otp" not in params else "token" if "token" not in params else None
        #     if nott:
        #         return Response({
        #             "Error": f"params.{nott} polyasi to'ldirilmagan"
        #
        #         })
        #
        #     otp = OTP.objects.filter(key=params['token']).first()
        #     if not otp:
        #         return Response({
        #             "Error": f"Xato Token"
        #         })
        #     otp.state = "step_two"
        #     otp.save()
        #     now = datetime.datetime.now(datetime.timezone.utc)
        #     cr = otp.created_at
        #     if (now - cr).total_seconds() > 120:
        #         otp.is_expired = True
        #         otp.save()
        #         return Response({
        #             "Error": f"Kod eskirgan"
        #         })
        #
        #     if otp.is_expired:
        #         return Response({
        #             "Error": f"Kod eskirgan"
        #         })
        #
        #     key = otp.key.split("$")[1]
        #     otp_key = code_decoder(key, decode=True)
        #     if str(otp_key) != str(params['otp']):
        #         otp.tries += 1
        #         if otp.tries >= 3:
        #             otp.is_expired = True
        #
        #         otp.save()
        #         return Response({
        #             "Error": "Xato OTP"
        #         })
        #
        #     user = User.objects.filter(mobile=otp.mobile).first()
        #     otp.state = "confirmed"
        #     otp.save()
        #     if user:
        #         return Response({
        #             "is_registered": True
        #         })
        #     else:
        #         return Response({
        #             "is_registered": False
        #         })