% Facts
student(1, 'Alice').
student(2, 'Bob').
student(3, 'Charlie').

teacher(1, 'Mr. Smith').
teacher(2, 'Ms. Johnson').

subject('CS101', 'Computer Science').
subject('MA101', 'Mathematics').
subject('PH101', 'Physics').

% Relationships
teaches(1, 'CS101').  % Mr. Smith teaches Computer Science
teaches(2, 'MA101').  % Ms. Johnson teaches Mathematics

enrolled(1, 'CS101'). % Alice is enrolled in Computer Science
enrolled(2, 'MA101'). % Bob is enrolled in Mathematics
enrolled(3, 'CS101'). % Charlie is enrolled in Computer Science
enrolled(3, 'PH101').  % Charlie is enrolled in Physics

% Rules to retrieve information
student_subjects(StudentID, Subjects) :-
    findall(Subject, enrolled(StudentID, Subject), Subjects).

teacher_students(TeacherID, Students) :-
    findall(Student, 
        (teaches(TeacherID, Subject), enrolled(Student, Subject)), 
        Students).

% Example Queries
% ?- student_subjects(3, Subjects).
% ?- teacher_students(1, Students).
