from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.contrib.auth import get_user_model
from .serializers.user_serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken
from rest_framework.permissions import IsAuthenticated


User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password']) 
            user.save()
            return Response({"message": "User registered successfully!"}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {"email": user.email, "full_name": user.full_name}
            })
        return Response({"error": "Invalid credentials"}, status=400)




class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"})
        except Exception as e:
            return Response({"error": str(e)}, status=400)



class PasswordResetView(APIView):
    def post(self, request):
        """Отправка инструкции по сбросу пароля на email"""
        # Здесь вы добавите код отправки письма с токеном для сброса пароля
        pass



class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)






class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]



class ProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile



class InstructorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Получение данных об инструкторе"""
        instructor = request.user.profile.instructor
        if not instructor:
            return Response({"error": "Not an instructor"}, status=400)
        serializer = InstructorSerializer(instructor)
        return Response(serializer.data)





class StudentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Получение данных о студенте"""
        student = request.user.profile.student
        if not student:
            return Response({"error": "Not a student"}, status=400)
        serializer = StudentSerializer(student)
        return Response(serializer.data)





class GenerateOTPView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        otp, created = OTP.objects.get_or_create(user=request.user)
        otp.generate_otp()
        return Response({"otp_code": otp.otp_code, "expires_at": otp.expires_at})






class VerifyOTPView(APIView):
    def post(self, request):
        otp_code = request.data.get("otp_code")
        try:
            otp = OTP.objects.get(user=request.user)
            if otp.is_valid() and otp.otp_code == otp_code:
                return Response({"message": "OTP verified successfully!"})
            return Response({"error": "Invalid or expired OTP"}, status=400)
        except OTP.DoesNotExist:
            return Response({"error": "OTP not found"}, status=404)





from rest_framework import status
from users.models import Instructor
from .serializers.instructor_serializers import InstructorSerializer

class InstructorDetailView(APIView):
    def get(self, request, instructor_id):
        try:
            instructor = Instructor.objects.get(id=instructor_id)
            serializer = InstructorSerializer(instructor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Instructor.DoesNotExist:
            return Response({"error": "Instructor not found"}, status=status.HTTP_404_NOT_FOUND)
