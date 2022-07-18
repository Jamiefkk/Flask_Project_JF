class VisitsAttraction:

    def __init__( self, user, attraction, review, visited = None, id = None ):
        self.user = user
        self.attraction= attraction
        self.review = review
        self.visited = visited
        self.id = id