import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from courses.models import Course

class CourseDetailView(APIView):
    def get(self, request, course_id):
        try:
            # Получаем курс из базы данных
            course = Course.objects.get(id=course_id)

            # Запрашиваем данные об инструкторе через API user_service
            instructor_api_url = f"http://user_service:8000/api/users/instructors/{course.instructor_id}/"
            response = requests.get(instructor_api_url)

            if response.status_code == 200:
                instructor_data = response.json()
            else:
                instructor_data = {"error": "Unable to fetch instructor data"}

            # Формируем ответ
            data = {
                "course": {
                    "id": course.id,
                    "title": course.title,
                    "description": course.description,
                    "price": course.price,
                },
                "instructor": instructor_data
            }
            return Response(data, status=status.HTTP_200_OK)

        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
