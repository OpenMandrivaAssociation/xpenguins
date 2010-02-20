%define name xpenguins
%define version 2.2
%define release %mkrel 10

Summary: Cute little penguins that walk along the tops of your windows
Name: %{name}
Version: %{version}
Release: %{release}
license: GPL
Source0: %{name}-%{version}.tar.bz2
Source1: %name-32x32.png.bz2
Source2: %name-16x16.png.bz2
Source3: %name-48x48.png.bz2
Patch0: xpenguins-2.2-fix-str-fmt.patch
Group: Toys
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://xpenguins.seul.org/
BuildRequires: xpm-devel
BuildRequires: libx11-devel
BuildRequires: libxext-devel

%description
XPenguins animates a friendly family of penguins in your root window.
They drop in from the top of the screen, walk along the tops of your
windows, up the side of your windows, levitate, skateboard, and do
other similarly exciting things. XPenguins is now themeable so if
you're bored of penguins, try something else. The themes that come
with this package are "Penguins", "Classic Penguins" and "Turtles". 

%prep
%setup -q
%patch0 -p0

%build
# Note: when we compile the program it needs to know where the 
# data will be when finally installed.
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
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

bzip2 -dc %{SOURCE1} > %buildroot%{_iconsdir}/%{name}.png
bzip2 -dc %{SOURCE2} > %buildroot%{_miconsdir}/%{name}.png
bzip2 -dc %{SOURCE3} > %buildroot%{_liconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog lay-out-frames.scm
%attr(755,root,root) %{_bindir}/xpenguins
%{_mandir}/man1/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/themes
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

