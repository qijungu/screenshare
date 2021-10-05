/*
Copyright (C) 2021  Qijun Gu

This file is part of Screenshare.

Screenshare is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Screenshare is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Screenshare. If not, see <https://www.gnu.org/licenses/>.
*/

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
