$(document).ready(function(){
	var page_click = function() {
			load_page($(this).data("loadPageNum"));
			return false;
		},
		remove_click = function() {
			remove($(this).data("newsId"), function() {
				load_page(window.page_num);
			});
			return false;
		},
		load_page = function(page_num, success_callback) {
			$.ajax({
				dataType: 'json',
				url: '/' + page_num + '/',
				success: function( data ) {
					window.page_num = page_num;
					var result = $( "<ul/>", {
					    "class": "media-list",
					    html: data.news.join( "" )
					})
					$("ul.media-list").replaceWith(result);
					result = $( "<ul/>", {
					    "class": "pagination",
					    html: data.pagination
					})
					$("ul.pagination").replaceWith(result);
					renew_events();
				}
			})
		},
		remove = function(news_id, success_callback) {
			$.ajax({
				dataType: 'json',
				url: '/remove/' + news_id + '/',
				success: function(data) {
					if (data.success == true) {
						success_callback();
					}
				}
			})
		},
		renew_events = function() {
			$('a[data-trigger="load_page"]').click(page_click)
			$('a[class="remove"]').click(remove_click)
			$("[data-toggle='confirmation']").popConfirm();			
		};

	renew_events();

	
})