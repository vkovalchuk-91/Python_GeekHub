$(document).ready(function () {
    $('.decrease-btn, .increase-btn').on('click', function () {
        var productId = $(this).data('product-pk');
        var action = $(this).hasClass('decrease-btn') ? 'decrease' : 'increase';
        var price = $('.item-price[data-product-pk="' + productId + '"]').text();
        var cost = $('.item-cost[data-product-pk="' + productId + '"]').text();
        var total = $('.total-cost').text();

        $.ajax({
            type: 'POST',
            url: '/cart/ajax_change_quantity/',
            data: {
                'product_id': productId,
                'action': action,
                'price': price,
                'item-cost': cost,
                'total-cost': total
            },
            headers: {
                'X-CSRFToken': csrf_token
            },
            success: function (data) {
                $('.quantity[data-product-pk="' + productId + '"]').text(data.quantity);
                $('.item-cost[data-product-pk="' + productId + '"]').text(data.cost);
                $('.total-cost').html('<strong>' + data.total + '</strong>');
            },
            error: function (error) {
                console.log('Error:', error);
            }
        });
    });
});


$(document).ready(function () {
    $('.remove-btn').on('click', function () {
        var productId = $(this).data('product-pk');
        var cost = $('.item-cost[data-product-pk="' + productId + '"]').text();
        var total = $('.total-cost').text();

        $.ajax({
            type: 'POST',
            url: '/cart/ajax_remove_item/',
            data: {
                'product_id': productId,
                'item-cost': cost,
                'total-cost': total
            },
            headers: {
                'X-CSRFToken': csrf_token
            },
            success: function (data) {
                $('.table-row[data-product-pk="' + productId + '"]').remove();
                $('.total-cost').html('<strong>' + data.total + '</strong>');
            },
            error: function (error) {
                console.log('Error:', error);
            }
        });
    });
});


$(document).ready(function () {
    $('.clear-btn').on('click', function () {

        $.ajax({
            type: 'DELETE',
            url: '/cart/ajax_remove_item/',
            headers: {
                'X-CSRFToken': csrf_token
            },
            success: function () {
                $('.empty-cart').css('display', 'inline');
                $('.not-empty-cart').css('display', 'none');
            },
            error: function (error) {
                console.log('Error:', error);
            }
        });
    });
});