%define upstream_name    Digest
%define upstream_version 1.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Calculate digests of files
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(MIME::Base64)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


