# from django.contrib.auth import get_user_model
# User = get_user_model()
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from chemical.models import Project, Formula



class ProjectModelTest(TestCase):

#     def test_get_absolute_url(self):
#         project_ = Project.objects.create()
#         self.assertEqual(project_.get_absolute_url(), '/projects/%d/' % (project_.id,))


    def test_projects_can_have_owners(self):
        Project(user=User())  # should not raise


#     def test_project_owner_is_optional(self):
#         Project().full_clean()  # should not raise


#     def test_project_name_is_first_formula_text(self):
#         project_ = Project.objects.create()
#         Formula.objects.create(project=project_, name='first formula')
#         Formula.objects.create(project=project_, name='second formula')
#         self.assertEqual(project_.name, 'first formula')


#     def test_create_new_creates_project_and_first_formula(self):
#         Project.create_new(first_formula_text='new formula text')
#         new_formula = Formula.objects.first()
#         self.assertEqual(new_formula.text, 'new formula text')
#         new_project = Project.objects.first()
#         self.assertEqual(new_formula.list, new_project)


#     def test_create_new_optionally_saves_owner(self):
#         user = User.objects.create()
#         Project.create_new(first_formula_text='new formula text', owner=user)
#         new_project = Project.objects.first()
#         self.assertEqual(new_project.owner, user)


#     def test_create_returns_new_project_object(self):
#         returned = Project.create_new(first_formula_text='new formula text')
#         new_project = Project.objects.first()
#         self.assertEqual(returned, new_project)


#     def test_can_share_with_another_user(self):
#         project_ = Project.objects.create()
#         user = User.objects.create(email='a@b.com')
#         project_.shared_with.add('a@b.com')
#         project_in_db = Project.objects.get(id=project_.id)
#         self.assertIn(user, project_in_db.shared_with.all())