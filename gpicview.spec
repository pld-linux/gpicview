#
# Conditional build:
%bcond_with		gtk3		# build GTK+3 disables GTK+2
%bcond_without		gtk2	# build with GTK+2

%if %{with gtk3}
%undefine	with_gtk2
%endif

Summary:	GPicView: Picture viewer of LXDE
Name:		gpicview
Version:	0.2.4
Release:	1
License:	GPL v2, LGPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	b209e36531f89c48e3067b389699d4c7
URL:		http://wiki.lxde.org/en/GPicView
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
BuildRequires:	intltool
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPicView is the standard picture viewer of LXDE.

Features:
- Extremely lightweight and fast with low memory usage
- Very suitable for default image viewer of desktop system
- Simple and intuitive interface

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__intltoolize}
%configure \
	%{?with_gtk3:--enable-gtk3}
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# missing in glibc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/ui
%{_iconsdir}/*/*/apps/*.png
