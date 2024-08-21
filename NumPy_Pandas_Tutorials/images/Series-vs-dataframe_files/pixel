(function (n, l, d, u, q, b, s, ss, sm, sr, c, i) {
  if (typeof n !== 'undefined' && n.webdriver) return;
  if (l.protocol !== 'http:' && l.protocol !== 'https:') return;
  q = (l.search || '').replace(/^\?/, '').split('&');
  sr = d.referrer || '';
  for (i=0; i<q.length; i++){
    if (q[i].indexOf('utm_source=') === 0) {
      ss = q[i].substr(11);
    } else if (q[i].indexOf('utm_medium=') === 0) {
      sm = q[i].substr(11);
    }
  }
  if (/^(cpc|ppc|paidsearch|cpv|cpa|cpp|content-text|display|cpm|banner)$/.test(sm)){
    c = 'paid';
  } else if (/^(organic|email|affiliate|referral|social)$/.test(sm)){
    c = sm;
  } else if (/^(social|social-network|social-media|sm|social network|social media)$/.test(sm)){
    c = 'social';
  } else if (/\.(google|bing|yahoo|yandex|duckduckgo|baidu)\./.test(sr)){
    c = 'organic';
  } else if (/facebook.com|plus.google.com|plus.url.google.com|instagram.com|linkedin.com|myspace.com|reddit.com|stumbleupon.com|t.co|twitter.com/.test(sr)){
    c = 'social';
  } else if (!sr){
    c = 'direct';
  } else {
    c = '';
  }
  b = d.getElementsByTagName('body')[0];
  s = d.createElement('span');
  u += '?r='+encodeURIComponent(l.protocol+'//'+l.hostname+l.pathname);
  u += '&c='+c;
  s.innerHTML = '<img src="'+u+'" alt="" style="width:1px;height:1px;position:absolute;bottom:100%;right:100%;visibility:hidden;" />';
  b.appendChild(s)
})(navigator, window.location, document, 'https://grow.clearbitjs.com/api/c.gif');

if (window.location.href && window.location.href.indexOf('cbDebug=true') > -1) { alert('Script successfully installed') }
