#
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
%define		pnam	ImageView
Summary:	Gtk2::ImageView - Perl bindings to the GtkImageView image viewer widget
Summary(pl.UTF-8):	Gtk2::ImageView - Dowiązania Perla dla GtkImageView
Name:		perl-Gtk2-ImageView
Version:	0.04
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1351295fb6391345fba53c25065180ed
URL:		http://trac.bjourne.webfactional.com/
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	perl-Glib >= 1.00
BuildRequires:	perl-Gtk2 >= 1.00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:  gtkimageview-devel >= 1.6.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtk2::ImageView - Perl bindings to the GtkImageView image viewer widget.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk2/ImageView.pm
%dir %{perl_vendorarch}/Gtk2/ImageView
%{perl_vendorarch}/Gtk2/ImageView/Install
%dir %{perl_vendorarch}/auto/Gtk2/ImageView
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/ImageView/*.so
%{perl_vendorarch}/auto/Gtk2/ImageView/*.bs
%{_mandir}/man3/*
