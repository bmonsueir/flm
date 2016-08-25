
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from chemical.models import Specification, Attribute, Chemical


class ChemicalModelTest(TestCase):

    def test_default_text(self):
        chemical = Chemical()
        self.assertEqual(chemical.name, '')


    def test_specification_is_related_to_chemical(self):
        chemical_ = Chemical.objects.create()
        specification = Specification()
        specification.chemical = chemical_
        specification.save()
        self.assertIn(specification, chemical_.specification_set.all())

    def test_attribute_is_related_to_chemical(self):
        chemical_ = Chemical.objects.create()
        attribute = Attribute()
        attribute.chemical = chemical_
        attribute.save()
        self.assertIn(attribute, chemical_.attribute_set.all())


    def test_cannot_save_empty_chemical_specification(self):
        chemical_ = Chemical.objects.create()
        specification = Specification(project=chemical_, name='')
        with self.assertRaises(ValidationError):
            specification.save()
            specification.full_clean()
    
    def test_cannot_save_empty_chemical_attribute(self):
        chemical_ = Chemical.objects.create()
        attribute = Attribute(project=chemical_, name='')
        with self.assertRaises(ValidationError):
            attribute.save()
            attribute.full_clean()



    def test_duplicate_specification_are_invalid(self):
        chemical_ = Chemical.objects.create()
        Specification.objects.create(chemical=chemical_, book='bla')
        with self.assertRaises(ValidationError):
            specification = Specification(chemical=chemical_, book='bla')
            specification.full_clean()
            
    def test_duplicate_attribute_are_invalid(self):
        chemical_ = Chemical.objects.create()
        Attribute.objects.create(chemical=chemical_, book='bla')
        with self.assertRaises(ValidationError):
            attribute = Specification(chemical=chemical_, book='bla')
            attribute.full_clean()


    # def test_project_ordering(self):
    #     project1 = Project.objects.create()
    #     formula1 = Formula.objects.create(project=project1, book='i1')
    #     formula2 = Formula.objects.create(project=project1, book='formula 2')
    #     formula3 = Formula.objects.create(project=project1, book='3')
    #     self.assertEqual(
    #         list(Formula.objects.all()),
    #         [formula1, formula2, formula3]
    #     )


    # def test_string_representation(self):
    #     formula = Formula(book='some text')
    #     self.assertEqual(str(formula), 'some text')

