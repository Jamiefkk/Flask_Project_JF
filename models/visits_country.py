class VisitsCountry:

    def __init__( self, user, country, review, visited = None, id = None ):
        self.user = user
        self.country = country
        self.review = review
        self.visited = visited
        self.id = id

    def visit_none(self):
        self.visited = None

    def visit_want_to_visit(self):
        self.visited = "Want to visit"

    def visit_visited(self):
        self.visited = "Visited"
