from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.v1.auth.servise import BearerAuth
from api.v1.comment.serializer import Commentserializer
from base.formats import comment_format
from sayt.models import Comment, Product, Like


class CommentView(GenericAPIView):
    serializer_class = Commentserializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerAuth,)

    def post(self, request, *args, **kwargs):
        user = request.user
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

        if method == "commentadd":
            product_id = Product.objects.filter(pk=params["product_id"]).first()
            if not product_id:
                return Response({
                    "Error": "bu id da product yo'q"
                })

            root = Comment()
            root.user = user
            root.product = product_id
            root.text = params["text"]
            root.save()
            return Response({"saved": comment_format(root)})

        if method == "like":
            comment_id = Comment.objects.filter(pk=params["comment_id"]).first()
            if not comment_id:
                return Response({
                    "Error": "bu id da comment yo'q"
                })

            if params['liketype'] == "like":

                like = Like.objects.filter(commentary_id=comment_id, user_id=user.id).first()

                if like:
                    like.user = user
                    like.like = True
                    like.dislike = False
                    like.commentary = comment_id
                    like.save()
                else:
                    root = Like()
                    root.user = user
                    root.like = True
                    root.dislike = False
                    root.commentary = comment_id
                    root.save()
                return Response({
                    "succes": "liked"
                })

            if params['liketype'] == "dislike":

                like = Like.objects.filter(commentary_id=comment_id, user_id=user.id).first()

                if like:
                    like.user = user
                    like.like = False
                    like.dislike = True
                    like.commentary = comment_id
                    like.save()
                else:
                    root = Like()
                    root.user = user
                    root.like = False
                    root.dislike = True
                    root.commentary = comment_id
                    root.save()
                return Response({
                    "succes": "disliked"
                })




