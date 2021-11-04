"""Module which contain project mixins"""


class RedirectToSuccesUrlMixIn:
    """MixIn to get the url in the template to the previous page """
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data()
        kwargs['succes_url'] = self.get_success_url()
        return kwargs
