%define upstream_name    Encode-Detect
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    9

Summary:    An Encode::Encoding subclass that detects the encoding of data
License:    GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Encode/%{upstream_name}-%{upstream_version}.tar.bz2

Buildrequires:  perl-devel
Buildrequires:  perl(Module::Build)
Buildrequires:  perl(ExtUtils::CBuilder)
Buildrequires:  perl(Data::Dump)

%description
This Perl module is an Encode::Encoding subclass that uses
Encode::Detect::Detector to determine the charset of the input data and then
decodes it using the encoder of the detected charset.

It is similar to Encode::Guess, but does not require the configuration of a set
of expected encodings. Like Encode::Guess, it only supports decoding--it cannot
encode.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE
%{perl_vendorarch}/Encode
%{perl_vendorarch}/auto/Encode
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-6mdv2012.0
+ Revision: 765197
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-5
+ Revision: 763713
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-4
+ Revision: 667128
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.10.0-3mdv2011.0
+ Revision: 564432
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.10.0-2mdv2011.0
+ Revision: 555282
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.1
+ Revision: 403159
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.01-3mdv2009.1
+ Revision: 351720
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.01-2mdv2009.0
+ Revision: 265358
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.0
+ Revision: 212212
- update to new version 1.01

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.00-3mdv2008.1
+ Revision: 152069
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.00-2mdv2008.0
+ Revision: 67820
- rebuild


* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdv2007.0
+ Revision: 111298
- Import perl-Encode-Detect

* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdv2007.1
- first mdv release

