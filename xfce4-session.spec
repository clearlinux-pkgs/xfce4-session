#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-session
Version  : 4.18.0
Release  : 28
URL      : https://archive.xfce.org/src/xfce/xfce4-session/4.18/xfce4-session-4.18.0.tar.bz2
Source0  : https://archive.xfce.org/src/xfce/xfce4-session/4.18/xfce4-session-4.18.0.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-session-bin = %{version}-%{release}
Requires: xfce4-session-data = %{version}-%{release}
Requires: xfce4-session-license = %{version}-%{release}
Requires: xfce4-session-locales = %{version}-%{release}
Requires: xfce4-session-man = %{version}-%{release}
BuildRequires : gtk3-dev
BuildRequires : iceauth-bin
BuildRequires : intltool
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libwnck-1.0)
BuildRequires : pkgconfig(libwnck-3.0)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(x11)
BuildRequires : sed
Patch1: stateless.patch

%description
[![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.xfce.org/xfce/xfce4-session/-/blob/master/COPYING)

%package bin
Summary: bin components for the xfce4-session package.
Group: Binaries
Requires: xfce4-session-data = %{version}-%{release}
Requires: xfce4-session-license = %{version}-%{release}

%description bin
bin components for the xfce4-session package.


%package data
Summary: data components for the xfce4-session package.
Group: Data

%description data
data components for the xfce4-session package.


%package license
Summary: license components for the xfce4-session package.
Group: Default

%description license
license components for the xfce4-session package.


%package locales
Summary: locales components for the xfce4-session package.
Group: Default

%description locales
locales components for the xfce4-session package.


%package man
Summary: man components for the xfce4-session package.
Group: Default

%description man
man components for the xfce4-session package.


%prep
%setup -q -n xfce4-session-4.18.0
cd %{_builddir}/xfce4-session-4.18.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671142987
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1671142987
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfce4-session
cp %{_builddir}/xfce4-session-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xfce4-session/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install
%find_lang xfce4-session
## install_append content
mv %{buildroot}%{_sysconfdir}/xdg %{buildroot}%{_datadir}/.
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/xfce4/session/xfsm-shutdown-helper

%files bin
%defattr(-,root,root,-)
/usr/bin/startxfce4
/usr/bin/xfce4-session
/usr/bin/xfce4-session-logout
/usr/bin/xfce4-session-settings
/usr/bin/xflock4

%files data
%defattr(-,root,root,-)
/usr/share/applications/xfce-session-settings.desktop
/usr/share/applications/xfce4-session-logout.desktop
/usr/share/icons/hicolor/128x128/apps/org.xfce.session.png
/usr/share/icons/hicolor/16x16/apps/org.xfce.session.png
/usr/share/icons/hicolor/24x24/actions/xfsm-hibernate.png
/usr/share/icons/hicolor/24x24/actions/xfsm-lock.png
/usr/share/icons/hicolor/24x24/actions/xfsm-logout.png
/usr/share/icons/hicolor/24x24/actions/xfsm-reboot.png
/usr/share/icons/hicolor/24x24/actions/xfsm-shutdown.png
/usr/share/icons/hicolor/24x24/actions/xfsm-suspend.png
/usr/share/icons/hicolor/24x24/actions/xfsm-switch-user.png
/usr/share/icons/hicolor/24x24/apps/org.xfce.session.png
/usr/share/icons/hicolor/32x32/apps/org.xfce.session.png
/usr/share/icons/hicolor/48x48/actions/xfsm-hibernate.png
/usr/share/icons/hicolor/48x48/actions/xfsm-lock.png
/usr/share/icons/hicolor/48x48/actions/xfsm-logout.png
/usr/share/icons/hicolor/48x48/actions/xfsm-reboot.png
/usr/share/icons/hicolor/48x48/actions/xfsm-shutdown.png
/usr/share/icons/hicolor/48x48/actions/xfsm-suspend.png
/usr/share/icons/hicolor/48x48/actions/xfsm-switch-user.png
/usr/share/icons/hicolor/48x48/apps/org.xfce.session.png
/usr/share/icons/hicolor/scalable/apps/org.xfce.session.svg
/usr/share/xdg/autostart/xscreensaver.desktop
/usr/share/xdg/xfce4/Xft.xrdb
/usr/share/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml
/usr/share/xdg/xfce4/xinitrc
/usr/share/xsessions/xfce.desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfce4-session/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xfce4-session-logout.1
/usr/share/man/man1/xfce4-session.1

%files locales -f xfce4-session.lang
%defattr(-,root,root,-)

