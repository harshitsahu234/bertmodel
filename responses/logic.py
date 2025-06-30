def get_response(sentiment):
    if sentiment == 'POSITIVE':
        return "😊 Thanks for your feedback! [Leave a testimonial](#)"
    elif sentiment == 'NEGATIVE':
        return "😔 Sorry to hear that. [Click here to file a complaint](#)"
    else:
        return "🤖 How can I help you? [Visit help center](#)"
