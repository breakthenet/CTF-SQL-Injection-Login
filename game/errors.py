class ChallengeError(Exception):
    def __init__(self, *args, **kwargs):
        if 'etype' in kwargs:
            self.error_type = kwargs.pop('etype')
        else:
            self.error_type = None
        super(ChallengeError, self).__init__(*args,**kwargs)

    def serialize(self):
        resp = {
            'status': 'error',
            'message': unicode(self),
            "type": "unknown"
        }
        if self.error_type is not None:
            resp['type'] = self.error_type

        return resp
