%define modname	Encode-Detect
%define modver	1.01
%define debug_package %{nil}

Summary:	An Encode::Encoding subclass that detects the encoding of data
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	28
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/pod/Encode::Detect
Source0:	http://www.cpan.org/modules/by-module/Encode/%{modname}-%{modver}.tar.bz2
Buildrequires:	perl(Test::More)
Buildrequires:	perl-devel
Buildrequires:	perl(Module::Build)
Buildrequires:	perl(ExtUtils::CBuilder)
Buildrequires:	perl(Data::Dump)

%description
This Perl module is an Encode::Encoding subclass that uses
Encode::Detect::Detector to determine the charset of the input data and then
decodes it using the encoder of the detected charset.

It is similar to Encode::Guess, but does not require the configuration of a set
of expected encodings. Like Encode::Guess, it only supports decoding--it cannot
encode.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE
%{perl_vendorarch}/Encode
%{perl_vendorarch}/auto/Encode
%{_mandir}/man3/*

