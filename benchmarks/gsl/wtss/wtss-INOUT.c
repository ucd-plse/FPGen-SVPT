#include <stdio.h>
#include <gsl/gsl_statistics.h>
#include <assert.h>

extern "C" {
#include <quadmath.h>
}

#ifndef N
#define N 64
#endif

#define K N/2

#ifndef FB
#define FB 64
#endif

#if(FB==64)
#define FT double
#elif(FB==80)
#define FT long double
#endif

int
main(int argc, char *argv[])
{
  assert(argc == 3);

  int i;
  char *inname = argv[1];
  char *outname = argv[2];
  FILE *infile = fopen(inname, "r");
  FILE *outfile = fopen(outname, "w");

  FT data[K], w[K];
  FT wtss;

  for (i = 0 ; i < K ; i++) {
    __float128 in_data;
    fread(&in_data, sizeof(__float128), 1, infile);
    data[i] = (float) in_data;
  }

  for (i = 0 ; i < K ; i++) {
    __float128 in_data;
    fread(&in_data, sizeof(__float128), 1, infile);
    w[i] = (float) in_data;
  }

  fclose(infile);

  // library call
  #if(FB==64)
    wtss     = gsl_stats_wtss(w, 1, data, 1, K);
  #elif(FB==80)
    wtss     = gsl_stats_long_double_wtss(w, 1, data, 1, K);
  #else
    exit(-1);
  #endif

  //printf ("The sample wtss is %g\n", wtss);

  __float128 out_data;
  out_data = (__float128) wtss;
  fwrite(&out_data, sizeof(__float128), 1, outfile);
  fclose(outfile);

  return 0;
}
