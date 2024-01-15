"""
 Με τη βιβλιοθήκη sys μας δίνονται πληροφορίες για το λειτουργικό σύστημα,
 για παράδειγμα μπορούμε με την παρακάτω εντολή for να εκτυπώσουμε το path του συγκεκριμένου αρχείου.
"""
import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')
