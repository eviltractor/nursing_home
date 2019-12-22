
let testAjax = function() {
    $.ajax({
        type: 'post',
        url: '',
        data: {
            'name': 'Test User',
            'email': 'test@mail.com'
        },
        dataType: 'json',
        headers:
            {
                'X-CSRFToken': csrfToken
            },
        success: function (data) {
            console.log(data);
            $('#hello-text').append(data['text']);
        }

});
};