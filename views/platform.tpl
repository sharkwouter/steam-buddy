% rebase('base.tpl')

<a href="/platforms/{{platform.get_id()}}/new">
    <img src="/images/add.png" alt="Add new shortcut" title="Add new shortcut"></img>
</a>

% for app in apps:
    <a href="/platforms/{{platform.get_id()}}/edit/{{app.name}}">
        % if app.banner == None :
            <div class="missing {{app.hidden}}">
                <img src="/images/add.png" alt="{{app.name}}" title="{{app.name}}"></img>
                <span class="missing-text">{{app.name}}</span>
            </div>
        % else :
            <img class="{{app.hidden}}" src="{{app.banner}}" alt="{{app.name}}" title="{{app.name}}"></img>
    </a>
% end
