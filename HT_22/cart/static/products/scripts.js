$(document).ready(function () {
    $('.cart-btn, .decrease-btn, .increase-btn').on('click', function () {
        var productId = $(this).data('product-pk');
        var action = $(this).hasClass('decrease-btn') ? 'decrease' : 'increase';

        $.ajax({
            type: 'POST',
            url: '/cart/ajax_change_quantity/',
            data: {
                'product_id': productId,
                'action': action,
            },
            headers: {
                'X-CSRFToken': csrf_token
            },
            success: function (data) {
                if (data && data.quantity !== undefined) {
                    $('.cart-btn[data-product-pk="' + productId + '"]').css('display', 'none');
                    $('.decrease-btn[data-product-pk="' + productId + '"]').css('display', 'inline');
                    $('.increase-btn[data-product-pk="' + productId + '"]').css('display', 'inline');
                    $('.quantity[data-product-pk="' + productId + '"]').css('display', 'inline').text(data.quantity);
                } else {
                    $('.cart-btn[data-product-pk="' + productId + '"]').css('display', 'inline');
                    $('.decrease-btn[data-product-pk="' + productId + '"]').css('display', 'none');
                    $('.quantity[data-product-pk="' + productId + '"]').css('display', 'none');
                    $('.increase-btn[data-product-pk="' + productId + '"]').css('display', 'none');
                }
            },
            error: function (error) {
                console.log('Error:', error);
            }
        });
    });
});
