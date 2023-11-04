from unittest import TestCase,main

from project.student import Student

class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("PeterPan", {"English":["english beginer", "english intermediate"]})

    def test_student_init(self):
        self.assertEqual("PeterPan", self.student.name)
        self.assertEqual({"English": ["english beginer", "english intermediate"]}, self.student.courses)

    def test_student_init_with_courses_none(self):
        self.student = Student("PeterPan", None)
        self.assertEqual({}, self.student.courses)

    def test_enroll_method_when_course_is_present_with_add_courses_note_sets_different_than_Y_or_empty_string(self):
        self.assertEqual({"English": ["english beginer", "english intermediate"]}, self.student.courses)
        res = self.student.enroll("English", ["English advanced", "English for physicist"], "No")
        self.assertEqual({"English": ["english beginer", "english intermediate","English advanced", "English for physicist"]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.",res)


    def test_enroll_method_when_course_is_not_present_with_add_courses_note_sets_to_Y(self):
        self.assertEqual({"English": ["english beginer", "english intermediate"]}, self.student.courses)
        res = self.student.enroll("Math", ["Linear algebra", "Analytical geometry"], "Y")
        self.assertEqual({"English": ["english beginer", "english intermediate"],"Math":["Linear algebra", "Analytical geometry"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.",res)

    def test_enroll_method_when_course_is_not_present_with_add_courses_note_sets_to_empty_string(self):
        self.assertEqual({"English": ["english beginer", "english intermediate"]}, self.student.courses)
        res = self.student.enroll("Math", ["Linear algebra", "Analytical geometry"], "")
        self.assertEqual({"English": ["english beginer", "english intermediate"],"Math":["Linear algebra", "Analytical geometry"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.",res)

    def test_enroll_method_when_course_is_not_present_with_add_courses_note_notSets_to_empty_string_ot_Y(self):
        self.assertEqual({"English": ["english beginer", "english intermediate"]}, self.student.courses)
        res = self.student.enroll("Math", ["Linear algebra", "Analytical geometry"], "N")
        self.assertEqual(
            {"English": ["english beginer", "english intermediate"], "Math": []},
            self.student.courses)
        self.assertEqual("Course has been added.", res)


    def test_adding_notes(self):
        self.assertEqual({"English": ["english beginer", "english intermediate"]}, self.student.courses)
        res = self.student.add_notes("English", ["English advanced", "English for physicist"])
        self.assertEqual(
            {"English": ["english beginer", "english intermediate", ["English advanced", "English for physicist"]]},
            self.student.courses)
        self.assertEqual("Notes have been updated", res)

    def test_adding_notes_when_not_present_course(self):
        self.assertEqual({"English": ["english beginer", "english intermediate"]}, self.student.courses)
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Math", ["Linear algebra", "Geometry"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))


    def test_leave_course_if_course_not_present(self):
        self.assertEqual({"English": ["english beginer", "english intermediate"]}, self.student.courses)
        with self.assertRaises(Exception) as ex:
            res=self.student.leave_course("Math")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course(self):
        self.assertEqual({"English": ["english beginer", "english intermediate"]}, self.student.courses)
        res=self.student.leave_course("English")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", res)


if __name__ == "__main__":
    main()
