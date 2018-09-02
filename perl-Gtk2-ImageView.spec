%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
%define		pnam	ImageView
Summary:	Gtk2::ImageView - Perl bindings to the GtkImageView image viewer widget
Summary(pl.UTF-8):	Gtk2::ImageView - wiązania Perla do widgetu przeglądarki obrazów GtkImageView
Name:		perl-Gtk2-ImageView
Version:	0.05
Release:	13
License:	LGPL v3+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Gtk2/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7c961071b347b6a64b8351fdd87ec4c0
URL:		http://trac.bjourne.webfactional.com/
BuildRequires:	gtkimageview-devel >= 1.6.0
BuildRequires:	perl-ExtUtils-Depends >= 0.2
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib-devel >= 1.140
BuildRequires:	perl-Gtk2-devel >= 1.140
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gtkimageview >= 1.6.0
Requires:	perl-Glib >= 1.140
Requires:	perl-Gtk2 >= 1.140
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl bindings to the GtkImageView image viewer widget.

The Perl bindings follow the C API very closely.

%description -l pl.UTF-8
Wiązania Perla do widgetu przeglądarki obrazów GtkImageView.

Wiązania są bardzo bliskie API języka C.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/ImageView.pod \
	$RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/ImageView{,/*}/*.pod \
	$RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/Gdk/Pixbuf/Draw/Cache.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{perl_vendorarch}/Gtk2/ImageView.pm
%dir %{perl_vendorarch}/Gtk2/ImageView
%{perl_vendorarch}/Gtk2/ImageView/Install
%dir %{perl_vendorarch}/auto/Gtk2/ImageView
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/ImageView/ImageView.so
%{_mandir}/man3/Gtk2::Gdk::Pixbuf::Draw::Cache.3pm*
%{_mandir}/man3/Gtk2::ImageView*.3pm*
