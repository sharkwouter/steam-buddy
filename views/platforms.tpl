% rebase('base.tpl')

% for p in platforms:
	<a href="/platforms/{{p.get_id()}}"><img src="images/{{p.get_id()}}.png" alt="{{p.get_name()}}"></img></a>
% end
