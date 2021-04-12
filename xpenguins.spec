Summary: Cute little penguins that walk along the tops of your windows
Name: xpenguins
Version: 3.2.1
Release: 1
license: GPL
Source0: https://sourceforge.net/projects/xpenguins/files/%{name}-%{version}.tar.gz

Group: Toys
URL: http://xpenguins.seul.org/
BuildRequires: xpm-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gmodule-2.0)

%description
XPenguins animates a friendly family of penguins in your root window.
They drop in from the top of the screen, walk along the tops of your
windows, up the side of your windows, levitate, skateboard, and do
other similarly exciting things. XPenguins is now themeable so if
you're bored of penguins, try something else. The themes that come
with this package are "Penguins", "Classic Penguins" and "Turtles". 

%prep
%setup -q

%build
# Note: when we compile the program it needs to know where the 
# data will be when finally installed.
%configure
%make_build

%install
%make_install
mkdir -p  %buildroot{%{_datadir}/applications,%{_iconsdir},%{_miconsdir},%{_liconsdir}}
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{name}
Categories=Amusement;
Name=Xpenguins
Comment=Display penguins running on your desktop.
EOF

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog lay-out-frames.scm
%attr(755,root,root) %{_bindir}/xpenguins
%{_mandir}/man1/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/themes
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/applications/xpenguins.desktop
%{_datadir}/pixmaps/xpenguins.xpm



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2-11mdv2011.0
+ Revision: 615730
- the mass rebuild of 2010.1 packages

* Sat Feb 20 2010 Funda Wang <fwang@mandriva.org> 2.2-10mdv2010.1
+ Revision: 508756
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 2.2-9mdv2009.0
+ Revision: 262683
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.2-8mdv2009.0
+ Revision: 257669
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 2.2-6mdv2008.1
+ Revision: 135561
- fix directory creation
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import xpenguins


* Thu Jan 05 2006 Lenny Cartier <lenny@mandriva.com> 2.2-6mdk
- rebuild

* Fri Jul 02 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.2-5mdk
- rebuild

* Sun Jun 15 2003 Götz Waschk <waschk@linux-mandrake.com> 2.2-4mdk
- arrgh, forgot to type C-c C-r

* Sat Jun 14 2003 Götz Waschk <waschk@linux-mandrake.com> 2.2-3mdk
- add the data dir
- add buildrequires
- remove prefix

* Mon Sep  9 2002 Arnaud Desmons <adesmons@mandrakesoft.com> 2.2-3mdk
- added Packager

* Mon Mar  4 2002 Götz Waschk <waschk@linux-mandrake.com> 2.2-2mdk
- substitute xpm by png icons
- fix data dir by using %%makeinstall_std macro

* Tue Oct 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.2-1mdk
- fixed & updated by Götz Waschk <waschk@linux-mandrake.com> :
	- fixed rpmlint warning about non-transparent icon
	- 2.2

* Fri Jun 22 2001 Etienne Faure <etienne@mandrakesoft.com> 2.1-2mdk
- large icon

* Fri Jun 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.1-1mdk
 
 - added in contribs bu Götz Waschk <waschk@linux-mandrake.com> :
         - adapted package for Mandrake

* Sat May  5 2001 Robin Hogan <R.J.Hogan@reading.ac.uk> 1.9.1-1
- First spec file used with autoconf
* Tue May 23 2000 Robin Hogan <R.J.Hogan@reading.ac.uk> 1.2-1
- Use BuildRoot.

# end of file
