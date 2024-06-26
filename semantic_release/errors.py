"""Custom Errors"""


class SemanticReleaseBaseError(Exception):
    """
    Base Exception from which all other custom Exceptions defined in semantic_release
    inherit
    """


class InvalidConfiguration(SemanticReleaseBaseError):
    """Raised when configuration is deemed invalid"""


class InvalidVersion(ValueError, SemanticReleaseBaseError):
    """
    Raised when Version.parse attempts to parse a string containing
    an invalid version.
    """


class NotAReleaseBranch(InvalidConfiguration):
    """
    Raised when semantic_release is invoked on a branch which isn't configured for
    releases
    """


class CommitParseError(SemanticReleaseBaseError):
    """
    Raised when a commit cannot be parsed by a commit parser. Custom commit parsers
    should also raise this Exception
    """


class MissingMergeBaseError(SemanticReleaseBaseError):
    """
    Raised when the merge base cannot be found with the current history. Generally
    because of a shallow git clone.
    """


class UnexpectedResponse(Exception):
    """
    Raised when an HTTP response cannot be parsed properly or the expected structure
    is not found.
    """
