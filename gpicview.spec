Summary:	GPicView: Picture viewer of LXDE
Name:		gpicview
Version:	0.2.1
Release:	0.1
License:	GPL v2, LGPL
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/project/lxde/GPicView%20%28image%20Viewer%29/GPicView%20%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a2de255bf9bdc40746c0dc89b3454a10
URL:		http://wiki.lxde.org/en/GPicView
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPicView is the standard picture viewer of LXDE. GPicView features
lightening fast startup and intuitive interface.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__intltoolize}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/ui
%{_pixmapsdir}/%{name}.png
