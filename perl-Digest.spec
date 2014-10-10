%define upstream_name    Digest
%define upstream_version 1.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Calculate digests of files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(MIME::Base64)
BuildArch:	noarch

%description
The 'Digest::' modules calculate digests, also called "fingerprints" or
"hashes", of some data, called a message. The digest is (usually) some
small/fixed size string. The actual size of the digest depend of the
algorithm used. The message is simply a sequence of arbitrary bytes or
bits.

An important property of the digest algorithms is that the digest is
_likely_ to change if the message change in some way. Another property is
that digest functions are one-way functions, that is it should be _hard_ to
find a message that correspond to some given digest. Algorithms differ in
how "likely" and how "hard", as well as how efficient they are to compute.

Note that the properties of the algorithms change over time, as the
algorithms are analyzed and machines grow faster. If your application for
instance depends on it being "impossible" to generate the same digest for a
different message it is wise to make it easy to plug in stronger algorithms
as the one used grow weaker. Using the interface documented here should
make it easy to change algorithms later.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.160.0-3mdv2011.0
+ Revision: 658746
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-2mdv2011.0
+ Revision: 552187
- rebuild

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2010.0
+ Revision: 395252
- import perl-Digest


* Sun Jul 12 2009 cpan2dist 1.16-1mdv
- initial mdv release, generated with cpan2dist
