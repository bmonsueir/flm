from django.contrib.auth import get_user_model
#User = get_user_model()
from django.core.exceptions import ValidationError
from django.test import TestCase
from chemical.models import Project, Formula


class FormulaModelTest(TestCase):

    def test_default_text(self):
        project = Project()
        self.assertEqual(project.name, '')


    def test_formula_is_related_to_project(self):
        project_ = Project.objects.create()
        formula = Formula()
        formula.list = project_
        formula.save()
        self.assertIn(formula, project_.formula_set.all())


    def test_cannot_save_empty_project_formulas(self):
        project_ = Project.objects.create()
        formula = Formula(list=project_, text='')
        with self.assertRaises(ValidationError):
            formula.save()
            formula.full_clean()



#     def test_duplicate_formulas_are_invalid(self):
#         project_ = Project.objects.create()
#         Formula.objects.create(list=project_, text='bla')
#         with self.assertRaises(ValidationError):
#             formula = Formula(list=project_, text='bla')
#             formula.full_clean()


#     def test_CAN_save_same_formula_to_different_projects(self):
#         project1 = Project.objects.create()
#         project2 = Project.objects.create()
#         Formula.objects.create(list=project1, text='bla')
#         formula = Formula(list=project2, text='bla')
#         formula.full_clean()  # should not raise


#     def test_project_ordering(self):
#         project1 = Project.objects.create()
#         formula1 = Formula.objects.create(list=project1, text='i1')
#         formula2 = Formula.objects.create(list=project1, text='formula 2')
#         formula3 = Formula.objects.create(list=project1, text='3')
#         self.assertEqual(
#             list(Formula.objects.all()),
#             [formula1, formula2, formula3]
#         )


#     def test_string_representation(self):
#         formula = Formula(text='some text')
#         self.assertEqual(str(formula), 'some text')



# class ProjectModelTest(TestCase):

#     def test_get_absolute_url(self):
#         project_ = Project.objects.create()
#         self.assertEqual(project_.get_absolute_url(), '/projects/%d/' % (project_.id,))


#     def test_projects_can_have_owners(self):
#         Project(owner=User())  # should not raise


#     def test_project_owner_is_optional(self):
#         Project().full_clean()  # should not raise


#     def test_project_name_is_first_formula_text(self):
#         project_ = Project.objects.create()
#         Formula.objects.create(list=project_, text='first formula')
#         Formula.objects.create(list=project_, text='second formula')
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