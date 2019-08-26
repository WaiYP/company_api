from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import CompanySerializer,FavouriteSerializer,UserSerializer
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from .models import Company, Favourite, User

class  UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['POST'])
    def register (self,request):
        response = {'message': 'Register successfully! '}
        return Response(response, status=status.HTTP_200_OK)


class  CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['GET'])
    def search_by_name(self, request):
        if 'name' in request.data:
            name = request.data['name']
            comp = Company.objects.get(name=name)
            serializer = CompanySerializer(comp,many=False)
            response = {'message': 'Company By Name ','result':serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide name'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def favourite_list(self, request):
        companies = []
        user = User.objects.get(id=1)
        try:
            favourite = Favourite.objects.filter(user=user.id,mark=True)
            for fav in favourite:
                comp = Company.objects.get(id=fav.company.id)
                companies.append(comp)
            serializer = CompanySerializer(companies, many=True)
            # serializer = FavouriteSerializer(fav,many=True)
            response = {'message': 'Company By Name ', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = {'message': 'You do not have favourite list' }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def fav_company(self, request, pk=None):
        if 'mark' in request.data:
            comp = Company.objects.get(id=pk)
            mark = request.data['mark']
            user = request.user

            try:
                fav = Favourite.objects.get(user=user.id, company=comp.id)
                fav.mark = mark
                fav.save()
                serializer = FavouriteSerializer(fav, many=False)
                response = {'message': 'Favourite updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                fav = Favourite.objects.create(user=user, company=comp, mark=mark)
                serializer = FavouriteSerializer(fav, many=False)
                response = {'message': 'Favourite created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide mark'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated,)