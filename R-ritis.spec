#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ritis
Version  : 1.0.0
Release  : 28
URL      : https://cran.r-project.org/src/contrib/ritis_1.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ritis_1.0.0.tar.gz
Summary  : Integrated Taxonomic Information System Client
Group    : Development/Tools
License  : MIT
Requires: R-crul
Requires: R-data.table
Requires: R-jsonlite
Requires: R-solrium
Requires: R-tibble
Requires: R-vcr
BuildRequires : R-crul
BuildRequires : R-data.table
BuildRequires : R-jsonlite
BuildRequires : R-solrium
BuildRequires : R-tibble
BuildRequires : R-vcr
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n ritis
cd %{_builddir}/ritis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612287935

%install
export SOURCE_DATE_EPOCH=1612287935
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ritis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ritis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ritis
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ritis || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ritis/DESCRIPTION
/usr/lib64/R/library/ritis/INDEX
/usr/lib64/R/library/ritis/LICENSE
/usr/lib64/R/library/ritis/Meta/Rd.rds
/usr/lib64/R/library/ritis/Meta/data.rds
/usr/lib64/R/library/ritis/Meta/features.rds
/usr/lib64/R/library/ritis/Meta/hsearch.rds
/usr/lib64/R/library/ritis/Meta/links.rds
/usr/lib64/R/library/ritis/Meta/nsInfo.rds
/usr/lib64/R/library/ritis/Meta/package.rds
/usr/lib64/R/library/ritis/NAMESPACE
/usr/lib64/R/library/ritis/NEWS.md
/usr/lib64/R/library/ritis/R/ritis
/usr/lib64/R/library/ritis/R/ritis.rdb
/usr/lib64/R/library/ritis/R/ritis.rdx
/usr/lib64/R/library/ritis/data/Rdata.rdb
/usr/lib64/R/library/ritis/data/Rdata.rds
/usr/lib64/R/library/ritis/data/Rdata.rdx
/usr/lib64/R/library/ritis/help/AnIndex
/usr/lib64/R/library/ritis/help/aliases.rds
/usr/lib64/R/library/ritis/help/paths.rds
/usr/lib64/R/library/ritis/help/ritis.rdb
/usr/lib64/R/library/ritis/help/ritis.rdx
/usr/lib64/R/library/ritis/html/00Index.html
/usr/lib64/R/library/ritis/html/R.css
/usr/lib64/R/library/ritis/tests/fixtures/accepted_names-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/accepted_names-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/accepted_names-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/accepted_names.yml
/usr/lib64/R/library/ritis/tests/fixtures/any_match_count-fails-well.yml
/usr/lib64/R/library/ritis/tests/fixtures/any_match_count-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/any_match_count-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/any_match_count.yml
/usr/lib64/R/library/ritis/tests/fixtures/comment_detail-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/comment_detail-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/comment_detail-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/comment_detail.yml
/usr/lib64/R/library/ritis/tests/fixtures/common_names-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/common_names-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/common_names-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/common_names.yml
/usr/lib64/R/library/ritis/tests/fixtures/core_metadata-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/core_metadata-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/core_metadata-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/core_metadata.yml
/usr/lib64/R/library/ritis/tests/fixtures/coverage-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/coverage-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/coverage-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/coverage.yml
/usr/lib64/R/library/ritis/tests/fixtures/credibility_rating-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/credibility_rating-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/credibility_rating-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/credibility_rating.yml
/usr/lib64/R/library/ritis/tests/fixtures/credibility_ratings.yml
/usr/lib64/R/library/ritis/tests/fixtures/currency-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/currency-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/currency-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/currency.yml
/usr/lib64/R/library/ritis/tests/fixtures/date_data-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/date_data-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/date_data-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/date_data.yml
/usr/lib64/R/library/ritis/tests/fixtures/description-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/description-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/description.yml
/usr/lib64/R/library/ritis/tests/fixtures/experts-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/experts-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/experts-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/experts.yml
/usr/lib64/R/library/ritis/tests/fixtures/full_record-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/full_record_lsid.yml
/usr/lib64/R/library/ritis/tests/fixtures/full_record_tsn.yml
/usr/lib64/R/library/ritis/tests/fixtures/geographic_divisions-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/geographic_divisions-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/geographic_divisions-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/geographic_divisions.yml
/usr/lib64/R/library/ritis/tests/fixtures/geographic_values-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/geographic_values-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/geographic_values.yml
/usr/lib64/R/library/ritis/tests/fixtures/global_species_completeness-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/global_species_completeness-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/global_species_completeness-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/global_species_completeness.yml
/usr/lib64/R/library/ritis/tests/fixtures/hierarchy-fails-well.yml
/usr/lib64/R/library/ritis/tests/fixtures/hierarchy_down.yml
/usr/lib64/R/library/ritis/tests/fixtures/hierarchy_full.yml
/usr/lib64/R/library/ritis/tests/fixtures/hierarchy_up.yml
/usr/lib64/R/library/ritis/tests/fixtures/itis_facet.yml
/usr/lib64/R/library/ritis/tests/fixtures/itis_group-fails-well.yml
/usr/lib64/R/library/ritis/tests/fixtures/itis_group.yml
/usr/lib64/R/library/ritis/tests/fixtures/itis_highlight.yml
/usr/lib64/R/library/ritis/tests/fixtures/itis_search-fails-well.yml
/usr/lib64/R/library/ritis/tests/fixtures/itis_search.yml
/usr/lib64/R/library/ritis/tests/fixtures/jurisdiction_values.yml
/usr/lib64/R/library/ritis/tests/fixtures/jurisdictional_origin-fails-well.yml
/usr/lib64/R/library/ritis/tests/fixtures/jurisdictional_origin.yml
/usr/lib64/R/library/ritis/tests/fixtures/jurisdictional_origin_values.yml
/usr/lib64/R/library/ritis/tests/fixtures/kingdom_name-fails-well.yml
/usr/lib64/R/library/ritis/tests/fixtures/kingdom_name.yml
/usr/lib64/R/library/ritis/tests/fixtures/kingdom_names.yml
/usr/lib64/R/library/ritis/tests/fixtures/publications-fails-well.yml
/usr/lib64/R/library/ritis/tests/fixtures/publications-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/publications-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/publications.yml
/usr/lib64/R/library/ritis/tests/fixtures/record-fails-well.yml
/usr/lib64/R/library/ritis/tests/fixtures/record-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/record-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/record.yml
/usr/lib64/R/library/ritis/tests/fixtures/search_common-fails-well.yml
/usr/lib64/R/library/ritis/tests/fixtures/search_common-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/search_common-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/search_common.yml
/usr/lib64/R/library/ritis/tests/fixtures/search_scientific-fail-well.yml
/usr/lib64/R/library/ritis/tests/fixtures/search_scientific-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/search_scientific-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/search_scientific.yml
/usr/lib64/R/library/ritis/tests/fixtures/terms_both.yml
/usr/lib64/R/library/ritis/tests/fixtures/terms_common.yml
/usr/lib64/R/library/ritis/tests/fixtures/terms_scientific.yml
/usr/lib64/R/library/ritis/tests/fixtures/usage-errors.yml
/usr/lib64/R/library/ritis/tests/fixtures/usage-json.yml
/usr/lib64/R/library/ritis/tests/fixtures/usage-xml.yml
/usr/lib64/R/library/ritis/tests/fixtures/usage.yml
/usr/lib64/R/library/ritis/tests/test-all.R
/usr/lib64/R/library/ritis/tests/testthat/helper-ritis.R
/usr/lib64/R/library/ritis/tests/testthat/test-accepted_names.R
/usr/lib64/R/library/ritis/tests/testthat/test-any_match_count.R
/usr/lib64/R/library/ritis/tests/testthat/test-comment_detail.R
/usr/lib64/R/library/ritis/tests/testthat/test-common_names.R
/usr/lib64/R/library/ritis/tests/testthat/test-core_metadata.R
/usr/lib64/R/library/ritis/tests/testthat/test-coverage.R
/usr/lib64/R/library/ritis/tests/testthat/test-credibility_rating.R
/usr/lib64/R/library/ritis/tests/testthat/test-currency.R
/usr/lib64/R/library/ritis/tests/testthat/test-date_data.R
/usr/lib64/R/library/ritis/tests/testthat/test-description.R
/usr/lib64/R/library/ritis/tests/testthat/test-experts.R
/usr/lib64/R/library/ritis/tests/testthat/test-full_record.R
/usr/lib64/R/library/ritis/tests/testthat/test-geographic_divisions.R
/usr/lib64/R/library/ritis/tests/testthat/test-geographic_values.R
/usr/lib64/R/library/ritis/tests/testthat/test-global_species_completeness.R
/usr/lib64/R/library/ritis/tests/testthat/test-hierarchy.R
/usr/lib64/R/library/ritis/tests/testthat/test-itis_facet.R
/usr/lib64/R/library/ritis/tests/testthat/test-itis_group.R
/usr/lib64/R/library/ritis/tests/testthat/test-itis_highlight.R
/usr/lib64/R/library/ritis/tests/testthat/test-itis_search.R
/usr/lib64/R/library/ritis/tests/testthat/test-jurisdiction.R
/usr/lib64/R/library/ritis/tests/testthat/test-kingdoms.R
/usr/lib64/R/library/ritis/tests/testthat/test-publications.R
/usr/lib64/R/library/ritis/tests/testthat/test-record.R
/usr/lib64/R/library/ritis/tests/testthat/test-search_common.R
/usr/lib64/R/library/ritis/tests/testthat/test-search_scientific.R
/usr/lib64/R/library/ritis/tests/testthat/test-terms.R
/usr/lib64/R/library/ritis/tests/testthat/test-usage.R
