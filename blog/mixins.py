class RedirectToSuccesUrlMixIn:
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data()
        kwargs['succes_url'] = self.get_success_url()
        return kwargs