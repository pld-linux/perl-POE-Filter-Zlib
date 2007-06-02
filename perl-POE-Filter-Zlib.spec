#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Filter-Zlib
Summary:	POE::Filter::Zlib - A POE filter wrapped around Compress::Zlib
Summary(pl.UTF-8):	POE::Filter::Zlib - filtr POE zbudowany wokół Compress:Zlib
Name:		perl-POE-Filter-Zlib
Version:	1.90
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	358377a9b2fbc66cc180129694253e20
URL:		http://search.cpan.ogr/dist/POE-Filter-Zlib/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Compress-Zlib >= 1.34
BuildRequires:	perl-POE >= 0.38
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Filter::Zlib provides a POE filter for performing
compression/uncompression using Compress::Zlib. It is suitable for use
with POE::Filter::Stackable.

This filter is not ideal for streaming compressed data over sockets
etc. as it employs compress and uncompress zlib functions.
POE::Filter::Zlib::Stream is recommended for that type of activity.

%description -l pl.UTF-8
POE::Filter::Zlib udostępnia filtr POE do wykonywania kompresji i
dekompresji przy użyciu Compress:Zlib. Nadaje się do użycia wraz z
POE::Filter::Stackable.

Ten filtr nie jest idealny dla strumieniowych, skompresowanych danych
przesyłanych przez gniazda itp., jako że wykorzystuje funkcje compress
i uncompress zliba. Dla strumieni zalecany jest moduł
POE::Filter::Zlib::Stream.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Filter/*.pm
%{perl_vendorlib}/POE/Filter/Zlib
%{_mandir}/man3/*
