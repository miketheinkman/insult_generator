#!/usr/bin/Python
import sqlite3


# connect to database. Will create if not exists
# check_same_thread arg lets us use this connection elsewhere
conn = sqlite3.connect("insult_db.db", check_same_thread=False)


def add_field(table, field, add_string):
    """Add arbitrary field to arbitrary table. Using wildcards here leaves us vulnerable
    to SQL injection attacks. Since this app is for fun, I don't give a shit. Later we can
    cover how to prevent these types of attacks. Maybe we will try some attacks of our own
    to see how they work so we know how we can prevent them."""
    with conn as c:
        c.execute("CREATE TABLE IF NOT EXISTS {0} (_id integer primary key autoincrement,"
                  "{1} text, UNIQUE({1} COLLATE NOCASE))".format(table, field))
        c.execute("INSERT INTO {0} ({1}) VALUES ('{2}')".format(table, field, add_string))


def generate_insult():
    """Here we generate the insults using randomized SQL SELECT Statements"""

    # Declare variables to avoid "may be referenced before..." warnings
    adjective_2 = None
    directive = None
    adjective_1 = None
    same = True
    name = None

    # catching any exceptions
    try:
        # using with lets us avoid having to close the connection
        with conn as c:

            # randomly select rows
            directive_row = c.execute("SELECT * FROM directives ORDER BY RANDOM() LIMIT 1")
            adjective_1_row = c.execute("SELECT * FROM adjectives ORDER BY RANDOM() LIMIT 1")

            # iterate through cursor data
            for d in directive_row:

                # assign directive the value of the second element of the data row
                directive = d[1]

            for a1 in adjective_1_row:
                adjective_1 = a1[1]

            # make sure adjective_1 and adjective_2 are different
            # commands loop while same = True
            while same:
                adjective_2_row = c.execute("SELECT * FROM adjectives ORDER BY RANDOM() LIMIT 1")
                for a2 in adjective_2_row:
                    adjective_2 = a2[1]

                # if adjectives are not the same, same is set to False, which breaks the loop
                if adjective_1 != adjective_2:
                    same = False

            # random name
            name_row = c.execute("SELECT * FROM names ORDER BY RANDOM() LIMIT 1")
            for n in name_row:
                name = n[1]

            # construct insult string
            insult = "{0}, you {1} {2} {3}.".format(directive, adjective_1, adjective_2, name)

    # this except statement is really too broad, but for what we need it is fine.
    # if there is an error, the insult will be replaced with exception before it is returned
    except Exception as e:
        insult = e

    # return statements basically set the value of a function. If you think of a function like
    # a variable, the data returned is similar to the value of a variable. You can pass
    # functions as arguments, print them, use them as operands, etc
    return insult

if __name__ == "__main__":
    print generate_insult()
