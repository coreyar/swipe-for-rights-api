from apistar import typesystem


class UserVoteType(typesystem.Object):
    properties = {
        'bill_id': typesystem.string(description="Reference to the Bill being voted on"),
        'supports': typesystem.boolean(description="True if the User supports the Bill, False otherwise."),
    }
