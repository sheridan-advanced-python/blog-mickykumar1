from django.contrib import messages
#...

class FormViewExample(FormView):
    template_name = 'blog/form_example.html'
    form_class = forms.ExampleSignupForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Create a "success" message
        self.messages.add_message(
            request,
            messages.SUCCESS,
            'Thank you for signing up!'
        )
        # Continue with default behaviour
        return super().form_valid(form)
