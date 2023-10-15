from ..plugin import Plugin
import xbmc, xbmcgui, xbmcaddon
import json
import resolveurl

addon_id = xbmcaddon.Addon().getAddonInfo('id')
default_icon = xbmcaddon.Addon(addon_id).getAddonInfo('icon')
default_fanart = xbmcaddon.Addon(addon_id).getAddonInfo('fanart')


class default_play_video(Plugin):
    name = "default video playback"
    priority = 0

    def play_video(self, item):
        item = json.loads(item)
        link = item["link"]
        title = item["title"]
        thumbnail = item.get("thumbnail", default_icon)
        liz = xbmcgui.ListItem(title)
        liz.setInfo('video', {'Title': title})
        liz.setArt({'thumb': thumbnail, 'icon': thumbnail})

        if not resolveurl.HostedMediaFile(link).valid_url():
            return xbmc.Player().play(link,liz)
        url = resolveurl.HostedMediaFile(link).resolve()
        return xbmc.Player().play(url,liz)
       
       