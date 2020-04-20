const commentForm = document.querySelector('#comment-form');

async function commentFormSubmitHandler(event) {
  // Prevent submission
  event.preventDefault();

  // Get the form action attribute (URL to post to)
  const apiUrl = commentForm.action;

  // Create a FormData instance with entered data
  const formData = new FormData(commentForm);

  // Post comment to server using AJAX
  const response = await fetch(apiUrl, {
    method: 'POST',
    body: formData,
  });

  if (response.ok) {
    // Hide the form
    commentForm.hidden = true;

    // Create a success message and display
    const successMessage = document.createElement('p');
    successMessage.textContent = 'Your comment was sent!'
    commentForm.parentNode.append(successMessage);
  } else {
    const errorMessage = document.createElement('p');
    errorMessage.textContent = 'An error occurred. Please try again.'
    commentForm.parentNode.append(errorMessage);
  }
}

commentForm.addEventListener('submit', commentFormSubmitHandler);

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # Get the post object
    post = self.get_object()

    # Set the post field on the form
    comment_form = forms.CommentForm(initial={'post': post})
    comments = models.Comment.objects.filter(post=post)

    context['comment_form'] = comment_form
    context['comments'] = comments.order_by('-created')

    return context
