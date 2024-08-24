### Mini Course Dictionary ###

## Description: In this program, the user will input a course number and they will recieve information about that course, including course name, instructor, and time. The user will be notified 
    # if the course number inputed is invalid. This program uses match-case as well as key-value dictionary methods
  # Type one of the following course numbers: 'COP 2510', 'EGN 3000L', 'MAC 2281', 'MUH 3016', 'PHY 2048'


# tuple for following courses

course_nums = ('COP 2510', 'EGN 3000L', 'MAC 2281', 'MUH 3016', 'PHY 2048')

# num=key, name/instructor/times=value

name_nums_dict = {course_nums[0]:'Programming Concepts', course_nums[1]: 'Foundations of Engineering Lab',
                    course_nums[2]: 'Calculus I', course_nums[3]: 'Survey of Jazz',
                    course_nums[4]: 'General Physics I'}

name_instructor_dict = {course_nums[0]:'S. Small', course_nums[1]: 'J. Anderson', course_nums[2]: 'A. Makaryus',
                        course_nums[3]: 'A. Wilkins', course_nums[4]: 'G. Pradhan'}

name_times_dict = {course_nums[0]:'TR 8:00am – 9:15am', course_nums[1]: 'TR 11:00am – 12:15pm',
                      course_nums[2]: 'MW 9:30am – 10:45am ', course_nums[3]: 'online asynchronous',
                      course_nums[4]: 'TR 5:00pm – 6:15pm'}

course = input('Enter a Course Number: ')


match course:
    case 'COP 2510':
        print(f'The course details are:\nCourse Name: {name_nums_dict.get(course)}')
        print(f'Instructor: {name_instructor_dict.get(course)}')
        print(f'Class Times: {name_times_dict.get(course)}')
    case 'EGN 3000L':
        print(f'The course details are:\nCourse Name: {name_nums_dict.get(course)}')
        print(f'Instructor: {name_instructor_dict.get(course)}')
        print(f'Class Times: {name_times_dict.get(course)}')
    case 'MAC 2281':
        print(f'The course details are:\nCourse Name: {name_nums_dict.get(course)}')
        print(f'Instructor: {name_instructor_dict.get(course)}')
        print(f'Class Times: {name_times_dict.get(course)}')
    case 'MUH 3016':
        print(f'The course details are:\nCourse Name: {name_nums_dict.get(course)}')
        print(f'Instructor: {name_instructor_dict.get(course)}')
        print(f'Class Times: {name_times_dict.get(course)}')
    case 'PHY 2048':
        print(f'The course details are:\nCourse Name: {name_nums_dict.get(course)}')
        print(f'Instructor: {name_instructor_dict.get(course)}')
        print(f'Class Times: {name_times_dict.get(course)}')
    case _:
        print(f'{course} is an invalid course number.')


        





