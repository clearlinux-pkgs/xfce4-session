#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-session
Version  : 4.13.2
Release  : 20
URL      : http://archive.xfce.org/src/xfce/xfce4-session/4.13/xfce4-session-4.13.2.tar.bz2
Source0  : http://archive.xfce.org/src/xfce/xfce4-session/4.13/xfce4-session-4.13.2.tar.bz2
Summary  : A session manager for Xfce
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-session-bin = %{version}-%{release}
Requires: xfce4-session-data = %{version}-%{release}
Requires: xfce4-session-lib = %{version}-%{release}
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
BuildRequires : pkgconfig(libxfce4ui-1)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(x11)
BuildRequires : sed
Patch1: stateless.patch

%description
Session manager for the Xfce desktop environment.
Shutting down your computer using the session manager:
------------------------------------------------------
Since 4.1.5, the session manager supports only sudo(8)-based shutdown, other
method can be added by packagers if desired, just replace XfsmShutdownHelper
with your code. To be able to shutdown the computer, you must be listed
in the systems sudoers file, in particular, you must be allowed to execute
$HELPER_PATH_PREFIX/xfce4/session/xfsm-shutdown-helper as user root (where
$HELPER_PATH_PREFIX is the directory passed to configure with the
--with-helper-path-prefix option or /usr/local/lib by default).

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


%package dev
Summary: dev components for the xfce4-session package.
Group: Development
Requires: xfce4-session-lib = %{version}-%{release}
Requires: xfce4-session-bin = %{version}-%{release}
Requires: xfce4-session-data = %{version}-%{release}
Provides: xfce4-session-devel = %{version}-%{release}
Requires: xfce4-session = %{version}-%{release}
Requires: xfce4-session = %{version}-%{release}

%description dev
dev components for the xfce4-session package.


%package lib
Summary: lib components for the xfce4-session package.
Group: Libraries
Requires: xfce4-session-data = %{version}-%{release}
Requires: xfce4-session-license = %{version}-%{release}

%description lib
lib components for the xfce4-session package.


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
%setup -q -n xfce4-session-4.13.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1558348673
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1558348673
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfce4-session
cp COPYING %{buildroot}/usr/share/package-licenses/xfce4-session/COPYING
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
/usr/share/icons/hicolor/128x128/apps/xfce4-session.png
/usr/share/icons/hicolor/48x48/actions/xfsm-hibernate.png
/usr/share/icons/hicolor/48x48/actions/xfsm-logout.png
/usr/share/icons/hicolor/48x48/actions/xfsm-reboot.png
/usr/share/icons/hicolor/48x48/actions/xfsm-shutdown.png
/usr/share/icons/hicolor/48x48/actions/xfsm-suspend.png
/usr/share/icons/hicolor/48x48/apps/xfce4-session.png
/usr/share/icons/hicolor/scalable/apps/xfce4-session.svg
/usr/share/xdg/autostart/xscreensaver.desktop
/usr/share/xdg/xfce4/Xft.xrdb
/usr/share/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml
/usr/share/xdg/xfce4/xinitrc
/usr/share/xsessions/xfce.desktop

%files dev
%defattr(-,root,root,-)
/usr/lib64/libxfsm-4.6.so
/usr/lib64/pkgconfig/xfce4-session-2.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxfsm-4.6.so.0
/usr/lib64/libxfsm-4.6.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfce4-session/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xfce4-session-logout.1
/usr/share/man/man1/xfce4-session.1

%files locales -f xfce4-session.lang
%defattr(-,root,root,-)

