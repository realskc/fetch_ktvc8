(function(){
	let demo = document.querySelector('#demo');
	let str = '';
	let cnt = 0;
	for (let i of demo.children) {
		if (i.tagName != 'IMG') continue;
		++cnt;
		url = i.src;
		str += url + '\n';
	}
	str = String(cnt) + '\n' + str;
	console.log(str);
})();