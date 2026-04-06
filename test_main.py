from main import get_median_coffee, get_all_rows

def test_median_for_one_student():
    rows = [
        {'student': 'Алексей Смирнов', 'date': '2024-06-01', 'coffee_spent': 450, 'sleep_hours': 4.5, 'study_hours': 12.0, 'mood': 'норм', 'exam': 'Математика'},
        {'student': 'Алексей Смирнов', 'date': '2024-06-02', 'coffee_spent': 500, 'sleep_hours': 4.0, 'study_hours': 14.0, 'mood': 'устал', 'exam': 'Математика'},
        {'student': 'Алексей Смирнов', 'date': '2024-06-03', 'coffee_spent': 550, 'sleep_hours': 3.5, 'study_hours': 16.0, 'mood': 'зомби', 'exam': 'Математика'}
    ]
    result = get_median_coffee(rows)
    assert result == [('Алексей Смирнов', 500)]

def test_median_for_multiple_students():
    rows = [
        {'student': 'Дарья Петрова', 'date': '2024-06-01', 'coffee_spent': 200, 'sleep_hours': 7.0, 'study_hours': 6.0, 'mood': 'отл', 'exam': 'Математика'},
        {'student': 'Алексей Смирнов', 'date': '2024-06-02', 'coffee_spent': 500, 'sleep_hours': 4.0, 'study_hours': 14.0, 'mood': 'устал', 'exam': 'Математика'},
        {'student': 'Алексей Смирнов', 'date': '2024-06-03', 'coffee_spent': 550, 'sleep_hours': 3.5, 'study_hours': 16.0, 'mood': 'зомби', 'exam': 'Математика'}
    ]
    result = get_median_coffee(rows)
    assert result == [('Алексей Смирнов', 525), ('Дарья Петрова', 200)]

def test_read_rows_from_multiple_files():
    files = ['test1.csv', 'test2.csv']
    result = get_all_rows(files)
    assert result == [{'student': 'Алексей Смирнов', 'date': '2024-06-01', 'coffee_spent': 450, 'sleep_hours': 4.5, 'study_hours': 12.0, 'mood': 'норм', 'exam': 'Математика'}, 
                      {'student': 'Алексей Смирнов', 'date': '2024-06-02', 'coffee_spent': 500, 'sleep_hours': 4.0, 'study_hours': 14.0, 'mood': 'устал', 'exam': 'Математика'},
                      {'student': 'Дарья Петрова', 'date': '2024-06-01', 'coffee_spent': 200, 'sleep_hours': 7.0, 'study_hours': 6.0, 'mood': 'отл', 'exam': 'Математика'}, 
                      {'student': 'Дарья Петрова', 'date': '2024-06-02', 'coffee_spent': 250, 'sleep_hours': 6.5, 'study_hours': 8.0, 'mood': 'норм', 'exam': 'Математика'}]