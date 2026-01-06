# Import any dependencies needed to execute sql queries
import pandas as pd
from employee_events.sql_execution import QueryMixin

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase(QueryMixin):

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ""

    # Define a `names` method that receives
    # no passed arguments
    def names(self) -> list[tuple]:
        return []
        
        # Return an empty list


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id: int) -> pd.DataFrame:     
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        sql_query_1 = f"""select event_date,
            SUM(positive_events) positive_events,
            SUM(negative_events) negative_events
            from employee_events
            where {self.name}_id = {id}
            group by event_date
            order by event_date
        """
        return self.pandas_query(sql_query_1)
            
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes(self, id: int) -> pd.DataFrame:

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        sql_query_2 = f"""select note_date, note
            from notes
            where {self.name}_id = {id}
            order by note_date
        """
        return self.pandas_query(sql_query_2)