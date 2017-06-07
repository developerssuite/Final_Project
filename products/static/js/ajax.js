/**
 * Created by Zohai on 5/10/2017.
 */
$(function () {

    $('#search').keyup(function () {
        $.ajax(
            {
                type: "POST",
                url: "/products/search/",
                data: {
                    'search_text' : $('#search').val(),
                    'csrfmiddlewaretoken' : $("input[name = csrfmiddlewaretoken]").val()
                },
                success: searchSuccess,
                dataType: 'html'
            });
        });
});

function searchSuccess(data, textStatus, jqXHR) {
    $('#search-results').html(data);

}

// $(function() {
//
//     $('#search').keyup(function() {
//
//         $.ajax({
//             type: "GET",
//             url: "/products/search/",
//             data: {
//                 'search_text' : $('#search').val(),
//                 'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
//             },
//             success: searchSuccess,
//             dataType: 'html'
//         });
//     });
// });
//
// function searchSuccess(data, textStatus, jqXHR)
// {
//     $('#search-results').html(data)
// }