var frameinterval = 200;     // 200 milliseconds means 5 frames per second
var frameerrcount = 0;
var screenfeedtimeout = null;

$(function() {
	screenfeed();
});

function screenfeed() {
	if (frameerrcount < 0) return;
	$.post('../screenfeed/')
	.then(function(r){
		ret = $.parseJSON(r);
		$('img.livescreen').attr('src', 'data:image/jpeg;base64,'+ret[1]);
		frameerrcount = 0;
		screenfeedtimeout = setTimeout(screenfeed, frameinterval)
	}, function(r) {
		if (frameerrcount < 0) return;
		frameerrcount++;
		screenfeedtimeout = setTimeout(screenfeed, frameinterval)
		if (frameerrcount > 20) {
			clearTimeout(screenfeedtimeout);
			frameerrcount = -1;
			$.alert({
			    title: 'Error!',
			    content: 'Lost screen from server. Refresh this page later...'
			});
		}
	});
}
