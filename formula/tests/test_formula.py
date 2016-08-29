# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
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
        formula.project = project_
        formula.save()
        self.assertIn(formula, project_.formula_set.all())


    def test_cannot_save_empty_project_formulas(self):
        project_ = Project.objects.create()
        formula = Formula(project=project_, book='')
        with self.assertRaises(ValidationError):
            formula.save()
            formula.full_clean()



    def test_duplicate_formulas_are_invalid(self):
        project_ = Project.objects.create()
        Formula.objects.create(project=project_, book='bla')
        with self.assertRaises(ValidationError):
            formula = Formula(project=project_, book='bla')
            formula.full_clean()


    def test_project_ordering(self):
        project1 = Project.objects.create()
        formula1 = Formula.objects.create(project=project1, book='i1')
        formula2 = Formula.objects.create(project=project1, book='formula 2')
        formula3 = Formula.objects.create(project=project1, book='3')
        self.assertEqual(
            list(Formula.objects.all()),
            [formula1, formula2, formula3]
        )


    def test_string_representation(self):
        formula = Formula(book='some text')
        self.assertEqual(str(formula), 'some text')

