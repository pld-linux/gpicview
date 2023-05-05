#
# Conditional build:
%bcond_with	gtk3	# use GTK+3 instead of GTK+2

Summary:	GPicView: Picture viewer of LXDE
Summary(pl.UTF-8):	GPicView - przeglądarka obrazków dla LXDE
Name:		gpicview
Version:	0.2.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	26be9b0c5a234f1afe7d83d02a4a33f4
URL:		https://lxde.sourceforge.net/gpicview/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libjpeg-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.12.0}
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPicView is the standard picture viewer of LXDE.

Features:
- Extremely lightweight and fast with low memory usage
- Very suitable for default image viewer of desktop system
- Simple and intuitive interface

%description -l pl.UTF-8
GPicView to standardowa przeglądarka obrazków środowiska LXDE.

Cechy:
- bardzo lekka, szybka, z małym zużyciem pamięci
- nadająca się jako domyślna przeglądardka obrazków środowiska
  graficznego
- prosty i intuicyjny interfejs

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_gtk3:--enable-gtk3} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unify names
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{tt_RU,tt}
# just a copy of ur
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpicview
%{_datadir}/gpicview
%{_desktopdir}/gpicview.desktop
%{_iconsdir}/hicolor/48x48/apps/gpicview.png
